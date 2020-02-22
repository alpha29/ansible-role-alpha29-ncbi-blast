ansible-role-ncbi-blast
=========

Installs NCBI BLAST.
- [Main page](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
- [Downloads](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
- [User manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)

Requirements
------------

This role requires root access, so either run it in a playbook with a global `become: yes`, or invoke the role in your playbook like:

    - hosts: localhost
      roles:
        - role: ansible-role-ncbi-blast
          become: yes

Role Variables
--------------

No configurable role variables at this time.

Dependencies
------------

See requirements.yml for third-party role dependencies.

Example Playbook
----------------

As above::

    - hosts: localhost
      roles:
        - role: ansible-role-ncbi-blast
          become: yes

Development
------------
```
# Setup:
python3.7 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
molecule test

# Usage:
# Do this to monitor timing, show Ansible debug logging, and tell Molecule to keep the Docker container on completion
time molecule --debug test --destroy=never

# Faster iterative development:
# Verify that you don't have a running container.
docker ps -a
# Create one.
time molecule create
# Run some tests, which should fail.
time molecule verify
# Just run the playbook - skip linting, tests, et cetera
time molecule converge
# Make some changes, lather, rinse, repeat.
...
time molecule converge
time molecule verify
...
# When finished, tear it down.
time molecule destroy

# By default, all of the above runs against a Centos 7 Docker image.  
# Use the MOLECULE_DISTRO environment variable to swap in other distros, e.g.: 
time MOLECULE_DISTRO=ubuntu1804 molecule test

# NOTE:  If you update requirements.yml, ***MAKE SURE*** you update meta/main.yml as well!
```

License
-------

MIT

Author Information
------------------

C.J. Brown (cbrown@alpha29.com)
