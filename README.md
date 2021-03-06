# Gen5CartsAPI
Python API wrapper for [gen5carts.com](https://gen5carts.com/apiDocs)

## Installation
Gen5CartsAPI is supported on python 2.7 (why are u still using py2?!) and py3+.

Clone the repo
```sh
$ sudo pip install -r requirements.txt
```

### Dependencies
* requests

### Prerequisites:
Gen5 API key; after registering it can be found
[here](https://gen5carts.com/apiDocs)

## Usage

### Authentication
    from gen5 import Gen5

    # Construct the Gen5 object
    gen5 = Gen5(api_key='YOUR_API_KEY')

### Examples

#### Uploading A Cart

    err, resp = gen5.upload_cart(site='Adidas US', email='email@gen5carts.com',
                                 password='password', price='25')

#### Retrieving Accounts

    err, accounts = gen5.retrieve_accounts(site='Adidas UK')
