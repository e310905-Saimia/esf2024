# ESF2024

This is the GitHub project for the course 

| ID | Name | Dates |
| ---- | ---- | ---- |
| AT00CK34-3003 | Embedded Systems | 2024-09-04 - 2024-12-31 |

## Repository usage

All content to the Git repository is made by using GitHub Issues. For each issue (new feature, bugfix etc.),
a branch called `feature/id-description-of-the-branch`, where `id` is the number (id) of the issue. After
the work described by the issue has been completed, the feature branch is merged to `main` and the feature
branch is removed from the server. 

The master branch is named `main`.

## Git commands

* To clone the repository (when using it for the first time): `git clone https://github.com/e310905-Saimia/esf2024.git`
* To check out a branch: `git checkout <branch_name>`
* Update list of branches from server: `git fetch --all`
* Observe Git history: `gitk` or `gitk --all` (adding `&` to the end detaches the `gitk` process from the terminal)
* Commit and push with GUI: `git gui`
   * Note: Adding new stuff to Git is a three-phase process. First you select the files to be included (`stage`), then you `commit` (to your local repository), and finally `push` the changes to the server

## Visibility

The project is public and visible to all.
