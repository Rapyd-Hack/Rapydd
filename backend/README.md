# The backend
----------------------------------------------------------------------------------------------------------

The backend was created to be partly REST API and clearnet.
Such that 
- Organizations(events/movie theatres or shows) can register crucial credentials on the platform, part of these credentials such as name and so on will be stored on our local database (SQLite).
While credentials containing specific id and bank details will be saved on rapyd. They are the default *beneficiaries*.

- Users only need to sign up with regular credentials. They are the default *senders* 

When an a theatre posts a ticket with its attched price and id, the user chooses the ticket and quantity, and checks out through rappyd that has been integrated.

The payout process occures between senders and beneficiaries i.e Theatres are trhe beneficiaries, who only posts tickets for checkout, and users are the senders that only buys ticket through rapyd checkout integrated.
 Most of the responses are in JSON format that should be gotten and visualized by the frontend.
