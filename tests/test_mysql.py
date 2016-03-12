import sys,os
sys.path.append(os.path.dirname(sys.path[0]))
from backend.mysql_model import db_mysql
from backend.mysql_model.user import User
#db_mysql.connect()
#db_mysql.connect()
#db_mysql.connect()
#db_mysql.create_tables([User,])
#db_mysql.close()
user=User.get_by_username('admin_test')

if user:
    user.delete_instance()
    print('already exist <admin_test>,so delete it!')
else:
    print('<admin_test> not exist')


user=User.new('admin_test','admin_test')
print('new user <admin_test:admin_test>',user)

user.set_password('root')
print('change <admin_test> password to <root>')

if User.auth('admin_test','admin'):
    print('auth success!')
else:
    print('auth failed!')


if User.exist('admin'):
    print('admin exist')
else:
    print('admin not exist')
print('User count ',User.count())
