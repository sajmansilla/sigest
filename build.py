from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")

name = "SiGeSt"
default_task = "publish"


@init
def initialize(project):
#   project.build_depends_on('mockito-without-hardcoded-distribute-version')
    project.build_depends_on('sqlalchemy')
    project.build_depends_on('psycopg2')

def set_properties(project):
    pass
