from mysql.scheme import User, session

def task_first():
    mass = session.query(User).filter(User.name.like('V%')).all()
    return mass

def task_second():
    return session.query(User).filter(User.salary < 17000).all()

def select_all():
    mass = session.query(User).all()
    return mass

def select_user(id_user):
    user = session.query(User).filter(User.id == id_user).first()
    return user

def delete_user(id_user):
    user = select_user(id_user)
    session.delete(user)
    session.commit()
    select_all()

def add_user(user):
    user_new = User(name=user[0], sorname=user[1], phone=user[3], age=user[2], salary=user[4])
    session.add(user_new)
    session.commit()
    select_all()

def update_user(user, id_user):
    delete_user(id_user)
    add_user(user)
    session.commit()
    select_all()

def numeration():
    mass = select_all()
    mass_numeration = []
    counter = 1
    for item in mass:
        mass_numeration.append(counter)
        counter = counter + 1
    return mass_numeration




