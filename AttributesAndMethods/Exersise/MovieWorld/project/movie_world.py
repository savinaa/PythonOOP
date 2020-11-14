class MovieWorld:
    def __init__(self, name):
            self.name = name
            self.customers=[]#Customer
            self.dvds=[] #DVD

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self,customer):
        if len(self.customers)<MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self,dvd):
        if len(self.dvds)<MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self,customer_id: int, dvd_id: int):
        for c in self.customers:
            if c.id==customer_id:
                customer=c
                break
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
                break

        if customer.age<dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        list_of_dvds = customer.rented_dvds
        for dvd_item in list_of_dvds:
            if dvd is dvd_item:
                return f"{customer.name} has already rented {dvd.name}"
        else:
            for cus in self.customers:
                if dvd in cus.rented_dvds and cus is not customer:
                    return f"DVD is already rented"
            else:
                customer.rented_dvds.append(dvd)
                dvd.is_rented=True
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self,customer_id, dvd_id):
        for c in self.customers:
            if c.id==customer_id:
                customer=c
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented=False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):

        output=""
        for customer in self.customers:
            output+=customer.__repr__()+"\n"
        for dvd in self.dvds:
            output+=dvd.__repr__()+'\n'

        return output