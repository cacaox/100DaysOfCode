class UsersController < ApplicationController

  def index
    @user = User.all #確認用
  end

  def new 
    @user = User.new
  end

  def create
    @user = User.new(user_params)
    if @user.save
        flash[:success] = "ユーザーを作成したんですよ！"
        session[:user_id] = @user.id
        redirect_to root_url
    end
  end

  private

  def user_params
    params.permit(:email, :name, :user_name, :password)
  end
end
