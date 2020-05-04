class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # print(var)
    # print(group.name)
    var = False
    return is_user_in_group_helper(user, group, var)


def is_user_in_group_helper(user, group, var):
    if user in group.get_users():       # Condition to check if users exist in the group.
        var = var or True
        return var

    if len(group.get_groups()):
        for groups in group.get_groups():
            var = is_user_in_group_helper(user, groups, var)       # Checking into all the groups by recursion.

    return False or var


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


is_user_in_group(sub_child_user, parent)  # return True
is_user_in_group(sub_child_user, child)  # return True
is_user_in_group(sub_child_user, sub_child)  # return True
is_user_in_group("child1", parent)  # return False