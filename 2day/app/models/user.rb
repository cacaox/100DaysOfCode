class User < ApplicationRecord
    VALID_EMAIL_RAGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
    
    validates :email, presence: true, uniqueness: { case_sensitive: false }, length: { maximum: 255 }, format: { with: VALID_EMAIL_RAGEX }
    validates :name, presence: true, length: { maximum: 30 }
    validates :nick_name, presence: true, length: { maximum: 30 }
    validates :password, presence: true, length: { minimum: 6 }
end
