from mysql.scheme import User, session

mass_query_first = session.query(User).filter(User.name.like('V%')).all()
mass_query_sod = session.query(User).filter(User.salary < 17000).all()

print(mass_query_sod)


