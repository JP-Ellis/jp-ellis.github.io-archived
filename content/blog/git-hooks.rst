=========
Git Hooks
=========

:date: 2015-12-08
:title: Git Hooks
:slug: git-hooks
:status: published
:tags: git

This blog is generated using Pelican_ which is based on Python_, and in order to
manage the differences between source code and the generated code, I use `git
hooks <https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`_.  I have it
setup so that whenever I run ``git push``, all the HTML files are regenerated
and a new commit is added and pushed in the ``master`` branch (which ultimately
becomes the HTML is this site).

.. _Pelican: http://getpelican.com/
.. _Python: https://python.org/

The following example goes through my setup with Github Pages, though it could
equivalently be used to push to another server, or anything else really since
the hook is a simple bash script.


Github Pages Setup
==================

I am using `Github Pages <https://pages.github.com/>`_ for this website which
serves the ``master`` branch from the repository called ``jp-ellis.github.io``.
I keep the source code in the ``source`` branch which is independent to the
``master`` branch (and similarly for the ``theme`` branch tracks [1]_).

The idea is to create separate repositories with separate branch names, and then
afterwards push them to the same remote repository:

.. code-block:: sh

   cd ~/web/jp-ellis.github.io
   # Setup git and create a new source branch
   git init .
   git checkout --orphan source
   git remote add origin git@github.com:JP-Ellis/jp-ellis.github.io.git
   # Setup the master branch
   git init ./output
   git remote add origin git@github.com:JP-Ellis/jp-ellis.github.io.git

At this stage, we have one repository inside the other.  We can make the parent
directory track the smaller directory with `submodules
<https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_.  This is not strictly
necessary in this case as the code in the parent repository doesn't rely on the
sub-repository; however, this can be quite useful if the sub-repository is used
as a dependency.  The submodule can be create with:

.. code-block:: sh

   cd ~/web/jp-ellis.github.io
   git submodule add git@github.com:JP-Ellis/jp-ellis.github.io.git ./output

At this stage, we can make all the changes to the code and commit them as usual,
and once ready we can commit the changes to the output and push everything.

.. code-block:: sh

   cd ~/web/jp-ellis.github.io
   # Make all the appropriate commits
   # Push the source and set upstream
   git push --set-upstream origin source
   cd output
   # Similarly, make appropriate commits and push
   git push --set-upstream origin master

At this stage, all the changes have been pushed to Github and the Github Pages
(assuming it has been enabled in the settings) should have updated and the
website is visible.  At this stage though, subsequent changes are annoying
because the commands in the last block of code have to be repeated every single
time---and knowing myself, I am bound to forget updating the output and pushing
the changes to the generated code.

Git Hooks
=========

In order to automate the process of pushing the source, regenerating the output
and pushing the output, I want to use `Git hooks
<https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`_.  Specifically, I
will have it setup such that every time I run ``git push`` in the source, all
the steps I run automatically.

The hooks are simple executable scripts located in ``.git/hooks/``.  By default,
new repositories have a few sample scripts which end in ``.sample`` which can be
put to use by removing the extension.

In my particular case, I want to regenerate the output through Pelican_,
automatically commit all the changes in the ``./output`` directory and finally
push both generated code and the source code.  The ``pre-push`` hook is what I
need for that as it is run before ``git push``.  The annotated content of my
``pre-push`` script is:

.. code-block:: sh

    #!/bin/sh

    # Get the short hash of the latest source commit
    commit_hash=$(git rev-parse --short HEAD)
    # Regenerate the output, and return an error if it fails (otherwise move on)
    make publish || return 1
    # Move to the output directory
    cd output
    # Tell git we're working on a different repository
    export GIT_WORK_TREE=$(pwd)
    # If there are no changes (i.e. git diff exist with 1),
    git diff --exit-code 2>&1 >/dev/null
    if [[ $? -eq 1 ]]; then
        # Stage, commit and push everything
        git add --all
        git commit -m "Update to ${commit_hash}."
        git push
    else
        echo "No changes to 'output'."
    fi

Finally, with all this setup I just need to run ``git push`` and the website will be automatically updated!


.. [1] The reason for the theme being tracked in a separate branch is that I may
       end up moving the branch to its own proper repository in the future, and
       I could do the same for the source branch though I think it makes more
       sense to keep the source and output in the same repositories.
