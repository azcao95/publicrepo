class VotesController < ApplicationController
  def create
    post_id = params[:post_id]
    vote = Vote.new
    vote.post_id = params[:post_id]
    vote.account_id = current_account.id
    

    #check if vote by this user exists
    existing_vote = Vote.where(account_id: current_account.id, post_id: params[:post_id])
    @existing_vote = existing_vote

    respond_to do |format|
      format.js{
        if existing_vote.size > 0
          #scorched earth destroy all existing votes
          existing_vote.each do |curr_vote|
            curr_vote.destroy
          end
        else
          #save new vote
          if vote.save
            @success = true
          else
            @success = false
          end
        end
        @post = Post.find(post_id)

        @is_upvote = params[:upvote]
        render partial: "votes/create"
      }
    end
  end

  def destroy
  
  end

  private

  def vote_params
    params.require(:vote).permit(:upvote, :post_id)
  end

end