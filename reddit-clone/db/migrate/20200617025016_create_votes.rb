class CreateVotes < ActiveRecord::Migration[6.0]
  def change
    create_table :votes do |t|
      t.references :account
      t.references :post
      t.boolean :upvote
      t.boolean :downvote

      t.timestamp
    end
  end
end
