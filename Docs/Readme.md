Command used for MongoDB Auth configuration:

```shell
use admin
db.createUser({ user:"admin", pwd:passwordPromt(), roles:[{role:"root", db:"admin"}] });
db.system.users.find()
db.system.users.deleteMany({})
```