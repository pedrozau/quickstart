import os 
import shutil 
import argparse 


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) 
PROJECT_FILES_DIR  = os.path.join(CURRENT_DIR,'..','project_files')


def create_project(project_name):
    os.makedirs(project_name) 
    shutil.copytree(PROJECT_FILES_DIR, os.path.join(project_name,'app'))
    print(f'Project {project_name} created successfully')

def main():
    parser = argparse.ArgumentParser(description="Generate a flask project.") 
    parser.add_argument('project_name',type=str,help='Name of the project')

    args = parser.parse_args()
    create_project(args.project_name)

if __name__ == "__main__":
    main()