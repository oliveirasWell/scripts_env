# Encontra recursivamente os diretorios que contem pom.xml.
# Caso o diretorio nao pussua pom.xml ignora ele e seus filhos.

import os

from util.directories import repos_directory
from util.urls import gists, repos


def recursive_maven_cleaner(directory):
    os.chdir(directory)
    if not 'pom.xml' in os.listdir('.'):
        os.chdir("..")
        return
    os.system("mvn clean")
    children = next(os.walk('.'))[1]
    for child in children:
        recursive_maven_cleaner(child)
    os.chdir("..")


def git_update(directory):
    os.chdir(directory)
    if not '.git' in os.listdir('.'):
        os.chdir("..")
        return
    os.system("git pull")
    os.chdir("..")


def clone_repositories(repositories):
    for repo in repositories:
        os.system('git clone ' + repo)


def update_and_clean_repositories():
    actual_directory = next(os.walk('.'))[1]
    for directory in actual_directory:
        print("------------------------------------------------------")
        print("Folder: " + directory)
        recursive_maven_cleaner(directory)
        git_update(directory)
        print("------------------------------------------------------")

    print("------------------------------------------------------")
    print("Updated Done")
    print("------------------------------------------------------")


def update_clone_gists():
    os.chdir('gist')
    update_and_clean_repositories()
    clone_repositories(gists)
    os.chdir('..')


def update_clone_repos():
    update_and_clean_repositories()
    clone_repositories(repos)


if __name__ == "__main__":
    os.chdir(repos_directory)
    update_clone_gists()
    update_clone_repos()
