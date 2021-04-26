# take first name and last name to title case
def format_name(fname, lname):
     """ This function takes two string inputs representing the first
     and last name, and returns the Title Case version of the name
     """
     if fname == "" or lname == "":
          return 'Invalid inputs provided.'
     fullname = f"{fname} {lname}".title()
     return fullname
