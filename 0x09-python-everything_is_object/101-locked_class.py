class LockedClass:
def __setattr__(self, name, value):
    if name == "first_name":
        super().__setattr__(name, value)
    else:
        raise AttributeError("Attribute cannot be created")
