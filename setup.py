from setuptools import find_packages, setup

package_name = 'arm_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@user.com',
    description='xArm6 teleoperation bridge',
    license='MIT',
    entry_points={
        'console_scripts': [
            'master  = arm_bridge.master_robot:main',
            'slave   = arm_bridge.slave_robot:main',
            'circle  = arm_bridge.circle_maker:main',
            'nettest = arm_bridge.net_test:main',
        ],
    },
)
