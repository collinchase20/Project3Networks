For this assignment our high level approach began by working through the first two milestone test cases. 
To start we set up print statements to understand the message types being received from the sockets that
were set up for us. Once understanding the message type, source, destination, and message we compared these to the
level one test cases to understand what to do.
We implemented support for UPdate messages which simply recieves a message, reads it, updates our forwarding table
(which was a dictionary of source: updatePacket) and then sends a update message to the other routers in our network.
Later we implemented code in this update message to determine what relationship we have and whether to send to all the
neighbors if our update was rdcieved as a customer or to only send to our customers if the update was recieved from a
peer or provider.
Next we implemented the forwarding of data messages to our neighbors. This consisted of finding the right route
in our established forwarding table and sending the correct formated message to our neighbors. After this we built
functionality for dump messages which sends our forwarding table so other destinations in our network can get this
data.
Next was the multiple methods for filtering routes. These were not too bad. It simply consisted of looping through all
the updates in our forwarding table and filtering them based on if the destination address and packet address were on the same
network we could then implement the filters. The hardest filter was probably the one to get the longest prefix
matching as this needed alot of conversions to binary.
The revoke message was not too bad after understanding how the update messages worked. It was almost the same logic except
instead of updating our forwarding table with the new entry we removed the entries from the revoke message from our forwarding
table and then sent the correct revoke messages to the correct neighboring routers.
The various rules for peering and provider relationships was easy. If the source was a customer we didnt need to change the
valid routes at all because we send to all neighbors here.
If the source relationship was a peer or provider then we checked to see if the destinaiton relationship was a customer in which
case we used the route but otherwise we do not.
Finally aggregation and disaggregation was difficult. Understanding how to check if routes were adjacent was alright
but actually modifying two adjacent routes was a tad tricky and figuring out how to make this flow work fluently when
there are multiple routes that could be coalesced was hard. Disaggregation was easier to implement once aggregation was there
but still interesting to understand the rebuilding and destroying of our forwarding table every time new revoke or
update messages came in.
The testing process was entirely up to interpreting the test cases given to us and understanding what the response should
be. Alot of times i found my self printing our the forwarding table i was returning and checking it against
the MISSING and EXTRA paths that the server was giving me as errors. This made it easy to understand where my logic
was going wrong when comparing the MISSING and EXTRA routes to the forwarding table we had returned.
