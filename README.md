This mini project was created in order to practice while watching the wonderful YouTube tutorial:

[Link to Corey Schafer YouTube tutorial](https://www.youtube.com/watch?v=JRCJ6RtE3xU)

***
## TIPS AND COMMENTS

* If you want to launch a **local debugging mail server**, instead of using your real email and the password that google
  provided you, you can do it with the `smtpd` python library:

      python3 -m smtpd -c DebuggingServer -n localhost:1025

  Which will be listening in the specified port. Then just change the line:

      smtplib.SMTP_SSL('smtp.gmail.com', port=465)

  with

      smtplib.SMTP('localhost', port=1025)
  You will not need to login. 

  **WARNING**: If you add attachments, they will appear in the debugging server as very long binary strings that will hide 
  the rest of the email. So the debugging server works better for just text emails.
* The html content of the body of the email is directly read from the file `resources/html_body_of_email.html`
