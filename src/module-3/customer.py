class Customer:

    def __init__(self,title,fname,lname,blacklisted):
        self.title=title
        self.firstName=fname
        self.lastName=lname
        self.blackListed=blacklisted

    def getBlacklisted(self):
        return self.blackListed
