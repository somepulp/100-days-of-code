
**Frequently performed commands:**

To delete a branch locally: 
`git branch -d localbranchname`

To delete a branch remotely:
`git push origin -delete localbranchname`

If a local branch has already been deleted remotely, synchronize your branch list using:
`git fetch -p`
-p = prune 