from google.appengine.api import mail

mail.send_mail(sender= "Slice@slice-cssi.appspotmail.com"
                   to=" {{ name }} < {{ email }}>",
                   subject="You've been Matched! -Slice",
                   body="""Dear {{ name }}:

      Congradulations! We found you someone in your area to order pizza with.

      Their email is {{ email }}, and we matched you with them based off the following preferences:

      - {{ num_ppl }}
      - {{ toppings }}
      - {{ location }}

      So what are you waiting for? That pizza won't order itself!


      Happy slicing,
      The Slice Team
""")
