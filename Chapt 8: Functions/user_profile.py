##Using Arbitary Keyword Arguments
#-Sometimes arbitary number of arguments will need to be passed but  the kind of information that will need to be passed to function won't be known.
#-In this case, functions that accept as many key-vakue pairs as the calling statement provides can be written

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location ='princeton',
                             field= 'physics')
print(user_profile)