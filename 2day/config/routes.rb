Rails.application.routes.draw do
  resources :products do
    member do
      get 'short'
      post 'toggle'
    end

    collection do
      get 'sold'
    end
  end

  resources :users

  root 'users#index'
end
