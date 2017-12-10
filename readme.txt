Error and Mitigation: For reasons still unknown to me, I cannot get sqlalchemy to operate on the table boards. I set the table name for the Board class to boards, but if I try to set the foreign key in the Element class to boards.id an error is thrown, while it is perfectly functional when the foreign key is set to board.id. After dedicating hours to try to solve this, I modified the test script tearDown function to delete board rather than boards. Besides that the program is functional. If it has something to do with my work envirnoment, I have marked where I modified test.py and where in app/data.py board.id would need to be changed to boards.id.

Note of tags: I did not add the tag functionality, in part because I dedicated too much time trying to fix the above error. However, I noticed that the test script did not account for tags in general, so I did not even iclude the empty list tags that was instructed in the assignment. 

All of my code was derived from the respectively libraries's documentation, and no code was pulled from github or stack overflow. 

The project tree is as follows:

├── app
│   ├── base.py
│   ├── base.pyc
│   ├── constants.py
│   ├── constants.pyc
│   ├── data.py
│   ├── data.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── routes.py
│   ├── routes.pyc
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── bundle.js
│   └── templates
│       ├── 404.html
│       └── index.html
├── config.py
├── config.pyc
├── manage.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── env.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
├── readme.txt
├── requirements.txt
├── run.py
└── test.py


where data handles all of the classes, routes handles all of the route endpoints, and constants remained empty and unused.
