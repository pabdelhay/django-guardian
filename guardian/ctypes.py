from django.contrib.contenttypes.models import ContentType

def get_ctype_from_polymorphic(obj):
    """
    Special helper function to return BASE polymorphic ctype id
    """
    if hasattr(obj, 'polymorphic_model_marker'):
        "For polymorphic models"
        superclasses = list(obj.__class__.mro())
        
        polymorphic_superclasses = list()
        for sclass in superclasses:
            if hasattr(sclass, 'polymorphic_model_marker'):
                polymorphic_superclasses.append(sclass)

        # PolymorphicMPTT adds an additional class between polymorphic and
        # base class
        if hasattr(obj, 'can_have_children'):
            root_polymorphic_class = polymorphic_superclasses[-3]
        else:
            root_polymorphic_class = polymorphic_superclasses[-2]
        ctype = ContentType.objects.get_for_model(root_polymorphic_class)

    else:    
        ctype = ContentType.objects.get_for_model(obj)

    return ctype