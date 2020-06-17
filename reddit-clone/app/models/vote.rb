class Vote < ApplicationRecord
  belongs_to :account
  belongs_to :post

  validates_uniqueness_of :account_id, scope: :post_id

  after_create :increment_upvote
  after_craete :increment_downvote
  after_destroy :decrement_upvote

  def increment_upvote
    Post.find(self.post_id).increment(:upvotes).save
  end

  def decrement_upvote
    Post.find(self.post_id).decrement(:upvotes).save
  end
end