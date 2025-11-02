# Nacos - Community

**Pages:** 5

---

## Community

**URL:** https://nacos.io/en-us/docs/community.html

**Contents:**
- Community
- Contact us
  - Nacos Gitter-https://gitter.im/alibaba/nacos
  - Nacos weibo-https://weibo.com/u/6574374908
  - Nacos segmentfault-https://segmentfault.com/t/nacos
  - Mailing list
  - Nacos DingDing group

Mailing list is recommended for discussing almost anything related to Nacos. Please refer to this?guide?for detailed documentation on how to subscribe to our mailing lists.

Welcome to join Nacos community nail group

---

## Developers

**URL:** https://nacos.io/en-us/docs/nacos-dev.html

**Contents:**
- Developers
- Nacos Developer Roles
  - Maintainer
  - Committer
  - Contributor
  - Nacos Developer Rights and Obligations
- Nacos Team
  - Committers
  - Contributors

Nacos developers include three roles: Maintainer, Committer, and Contributor. The standard definitions for each role are as follows.

Maintainer is an individual who has made a significant contribution to the evolution and development of the Nacos project, including projects under the nacos-group. Specifically includes the following criteria:

Committer is an individual with write access to the Nacos repository and includes the following criteria:

Contributor is an individual who contributes to the Nacos project. The standard is:

This page shows Nacos developers and continues to expand. The list is not prioritized.

---

## How to Contribute

**URL:** https://nacos.io/en-us/docs/contributing.html

**Contents:**
- How to Contribute
- Contact us
      - Nacos Gitter- https://gitter.im/alibaba/nacos
      - Nacos weibo- https://weibo.com/u/6574374908
      - Nacos segmentfault- https://segmentfault.com/t/nacos
    - Mailing list
- Contributing Code
  - Notice
    - Read Nacos Code of Conduct, and make sure your IDE has set code style and install plugin.
    - If the change is non-trivial, please include unit tests that cover the new functionality.

Nacos is released under the non-restrictive Apache 2.0 license, and follows a very standard Github development process, using Github tracker for issues and merging pull requests into master. If you want to contribute even something trivial, please do not hesitate, but follow the guidelines below.

We are always very happy to have contributions, whether for trivial cleanups or big new features. We want to have high quality, well documented codes for each programming language.

Nor is code the only way to contribute to the project. We strongly value documentation, integration with other project, and gladly accept improvements for these aspects.

Mailing list is recommended for discussing almost anything related to Nacos. Please refer to this?guide?for detailed documentation on how to subscribe to our mailing lists.

To submit a change for inclusion, please do the following:

This is a rough outline of what a contributor's workflow looks like:

Submit a pull request to alibaba/nacos and wait for reply.

Detail contribution flow see Contribution Flow

Thanks for contributing!

When contributing documents, please confirm and check the following:

We are always interested in adding new contributors. What we look for are series of contributions, good taste and ongoing interest in the project. If you are interested in becoming a committer, please let one of the existing committers know and they can help you walk through the process.

Nowadays, we have several important contribution points:

If you want to contribute to the above listing points, you must abide by the prerequisites listed below:

**Examples:**

Example 1 (unknown):
```unknown
git remote add upstream git@github.com:alibaba/nacos.git
git fetch upstream
git rebase upstream/master
git checkout -b your_awesome_patch
... add some work
git push origin your_awesome_patch
```

---

## Nacos Contributing Flow

**URL:** https://nacos.io/en-us/docs/contributing-flow.html

**Contents:**
- Nacos Contributing Flow
- 1. Fork Alibaba/Nacos repository to your Github.
- 2. Clone your fork Nacos repository to local.
- 3. Add Alibaba/Nacos repository as upstream repo.
- 4. Choose a basic branch of development usually upstream/develop,and create a new branch based on it.
- 5. Do your change in your local develop branch.
- 6. Rebase develop branch
- 7. Push your develop branch to your fork repository.
- 8. Create Pull Request according to the pull request template
- 9. If no more problem, Nacos community will merge your PR. Congratulations for you becoming a official contributor of Nacos.

This contribution flow is applicable to all Nacos community content, including but not limited to Nacos, Nacos wiki/doc, Nacos SDK.

The following use contributing Nacos as an example to explain the contribution flow in detail.

First please make sure you read and set the Nacos code style correctly, please read the related content Code of Conduct.

When making changes, please ensure that the changes on this branch are only relevant to the issue, and try to be as small as possible, so that only one thing is modified in one branch, and only one thing is modified in one PR.

At the same time, please use your English description as much as possible for your commits. It is mainly described by predicate + object, such as: Fix xxx problem/bug.

Some simple commits can be described using For xxx, such as: For codestyle.

If the commits is related to an ISSUE, you can add the ISSUE number as a prefix, such as: For #10000, Fix xxx problem/bug.

When you make changes, other people's changes may have commited and merged. At this time, there may be conflicts. Please use the rebase command to merge and resolve. There are two main benefits:

If you are using Intellij IDEA, it is recommended to use the IDE version control, which has a more convenient visual panel to resolve conflicts and squash operations.

pull request template

The Nacos community will review your Pull Request and may propose comments.

You can return to step 5 to modify code according to the comments and use step 6 to resubmit.

If you are prompted that there are conflicts when you push to fork repo again, Force push to your fork branch will be ok. The reason of conflicts is that the commit ID has changed after you rebase with others changes.

**Examples:**

Example 1 (unknown):
```unknown
git clone ${your fork nacos repo address}

cd nacos
```

Example 2 (unknown):
```unknown
git remote add upstream https://github.com/alibaba/nacos.git

git remote -v 

    origin	   ${your fork nacos repo address} (fetch)
    origin	   ${your fork nacos repo address} (push)
    upstream	https://github.com/alibaba/nacos.git (fetch)
    upstream	https://github.com/alibaba/nacos.git (push)
    
git fetch origin
git fetch upstream
```

Example 3 (unknown):
```unknown
(checkout branch from remote repo to local）
git checkout -b upstream-develop upstream/develop

(Create a development branch from the local branch, usually using the issue number as the development branch name）
git checkout -b develop-issue#${issue-number}
```

Example 4 (unknown):
```unknown
git fetch upstream

git rebase -i upstream/develop
```

---

## Reporting bugs

**URL:** https://nacos.io/en-us/docs/how-to-reporting-bugs.html

**Contents:**
- Reporting bugs
- Reporting security bugs

If any part of the Nacos project has bugs or documentation mistakes, please let us know by opening an issue. We treat bugs and mistakes very seriously and believe no issue is too small, anyOne is implement. Before creating a bug report, please check that an issue reporting the same problem does not already exist.

To make the bug report accurate and easy to understand, please try to create bug reports that are:

Specific. Include as much details as possible: which version, what environment, what configuration, etc. If the bug is related to running the Nacos server, please attach the Nacos log (the starting log with Nacos configuration is especially important).

Reproducible. Include the steps to reproduce the problem. We understand some issues might be hard to reproduce, please includes the steps that might lead to the problem. If possible, please attach the affected Nacos data dir and stack strace to the bug report.

Unique. Do not duplicate existing bug report.

It may be worthwhile to read Elika Etemad’s article on filing good bug reports before creating a bug report.

We might ask for further information to locate a bug. A duplicated bug report will be closed.

If you find any security problem in the Nacos project, please let us know through ASRC (Alibaba Security Response Center).

---
