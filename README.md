# django-playground

## How did it go notes

- Struggled to launch postgres for tests.
- Left a few `TODO` `FIXME` tags
- Finished right on time, didn't look over what would I change and how I would improve the app in detail
- Though one suggestion was the "mine addresses" can only be created when they are first searched, this is unnecessary IMO


## Description of the app
Purpose of this app is to allow users to manage their crypto addresses. User can look up transactions and addresses from blockchain, track their own addresses statuses and manage incoming orders. Order is a transaction that address owner is expecting to receive to provide some service for agreed price.

All app functionality should be implemented as an API. Django admin panel is as a helper for developer and not expected as a requirement.

App functionality:
* Allows user to register and login via API
* Blockchain querying
	* User can search address or transaction of ETH, BTC or BCH and show the addresses/transactions that involve this specific transaction/address and their values
	* User can get list of his past searches
* User address management
	* User can mark an address as ‘mine’.
	* User can get the balance aggregated by currency from all the addresses he selected as mine
* User can manage crypto orders
	* User can create an order with specific amount and with response user will get order id and deposit address. Deposit address is picked from marked as mine addresses and each open order has different deposit wallet address. After order completion address can be reused.
	* User can mark order as complete through API.