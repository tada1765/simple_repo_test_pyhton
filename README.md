# simple_repo_test_pyhton, Set up Virtual Environments.

Objective:
-----------
- To create a virtual environment to python project.

References:
-------------
- Python Tutorial: VENV (Windows) - How to Use Virtual Environments with the Built-In venv Module from Corey Schafer, [video here](https://www.youtube.com/watch?v=APOPm01BVrk)

Command:
-------------
- pip list
- python -m venv *project_env*
- dir
- project_env\Scripts\activate.bat
- where python
- pip install pytz
- cls
- pip freeze
- deactivate
- rmdir project_env /s
- mkdir my_project
- python -m venv my_python\venv
- my_project\venv\Scripts\activate.bat
- pip install -r requirement.txt
- rmdir ven /s
- python -m venv venv --system-site-packages


procedure create virtual environment with current packages:
-------------
1. win + r -> open cmd:
![cmd](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/a337d376e932881e6e73e89a641ec050/image.png)

2. go to desktop type: cd Desktop
![cd desktop](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/7c97e1f95640da96b78448b68b7ac24f/image.png)

3. create a file "first_project" type: mkdir first_project
![mkdir](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/a8d5ed6884f5784c63d7dc367f5a5e4a/image.png)

4. go to first_project type: cd first_project then create virtual environment by type: python -m venv venv --system-site-packages:
![python1](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/6720bc1cec793bc1e3adcb2011dcf428/image.png)

5. go to virtual environment and activate it by type: venv\Scripts\activate.bat
![activate](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/39eda8dc7fc9a8f3738851a2d8306ed5/image.png) 

6. check to installed packages type: pip list
![piplist](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/68e6fa117afd4f009bab7174b1d806e6/image.png)

7. then install new package type: pip install [package_name], to see the different  between virtual environment and your system environment.

8. your python script example: script.py should locate under here not inside venv folder.
![locate.py](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/ab37d8e08240ca4724732332cd23fde1/image.png)

9. to deactivate virtual environment type: deacivate, so you can back to system environment.
![deactivate](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/394c32b2ce7a193a41e82b1292b004de/image.png)

10. But the virtual environment still exist, to remove it type: rmdir venv /s
![remove](https://trello-attachments.s3.amazonaws.com/5d8b054c3d624239e7d6a5dc/5d917c2d33dd327c9cc296b7/007c063ee9ccb59e3a59c9afc6d5dcfa/image.png)

Summery:
------------
- This procedure mainly to create a virtual environment for a project, so every project will have separate packages that will not mashup your system environment.
- it is save memory space for a project only install packages that is needed.
