#clone the repository in gitbash:

git clone git@github.com:SabujPaul/newTask.git

#now open terminal:

cd newTask

#Activate vartual environment:

venv/Scripts/Activate

cd task_manager

python manage.py migrate

python manage.py runserver


List of Endpoints

/api/tasks/: List all tasks. Create new task.

/api/tasks/<task_id>/: Retrieve a single task. Delete task. Update task.

/api/photos/: list of all images. Post new image.

/api/photos/photo_id: Retrieve a single image. delete exixting image.
