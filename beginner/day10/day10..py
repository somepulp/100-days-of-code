# take first name and last name to title case
def format_name(fname, lname):
     if fname == "" or lname == "":
          return 'Invalid inputs provided.'
     fullname = f"{fname} {lname}".title()
     return fullname
