import pickle

filename = "data.pickle"


def add_or_update_entity(entity):
    """

    :param entity: the required entity to add with entities Type : [customer,flight,vehicle,hotel,bundle]
    :return: void
    """

    entity_type = entity.__class__.__name__

    with open(filename, 'rb+') as file:
        try:
            data = pickle.load(file)
            try:

                if entity_type in data:
                    data[entity_type][entity.id] = entity

                else:
                    data[entity_type] = {entity.id: entity}

            except KeyError:
                data[entity_type] = {entity.id: entity}
        except EOFError:
            data = {entity: {entity.id: entity}}

    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    # print("Entity has been added successfully ! ")


def get_entity_by_id(id, entity):

    """
    :param id: string with the id of the entity
    :param entity: string with the name of the object type e.g : Customer, Flight etc..
    :return: return the entity object with the required id if exist, and None if isnt.
    """

    with open(filename, 'rb') as file:
        data = pickle.load(file)
    if entity in data:
        all_certain_entity = data[entity]
    else:
        return None
    if id in all_certain_entity:
        return all_certain_entity[id]
    return None


def get_entities_list_by_property(property, entity, value):
    """
    :param property: String with the property name
    :param entity:  String with the name of the entity class , e.g : Customer, Flight
    :param value: The required value to append to the list
    :return: list with all the required entity by the property
    """
    required_data = []
    all_certain_entity = get_all_certain_entity(entity)
    for item in all_certain_entity.values():
        temp_item = getattr(item, property)
        if temp_item == value:
            required_data.append(item)

    return required_data


def get_entity_list_by_properties(entity, **kwargs):
    results_list = []
    all_entity_data = [x for x in get_all_certain_entity(entity).values()]

    for item in all_entity_data:
        flag = True
        for key in kwargs:
            # print(key)
            # print(kwargs[key])
            # print(getattr(item,key))
            if kwargs[key]==None or kwargs[key]=="":
                continue
            if key=="room_beds" or key=="stars" or key=="max_seats":
                if int(getattr(item,key))<int(kwargs[key]):
                    flag=False
            elif  key=="price":
                if int(getattr(item, key)) > int(kwargs[key]):
                    flag=False
            elif getattr(item,key)!=kwargs[key]:

                flag=False
        if flag:
            results_list.append(item)
    return results_list


def get_all_certain_entity(entity):
    """
    :param entity: string with the required entity type e.g Customer, Flight
    :return:
    """

    with open(filename, 'rb+') as file:
        try:
            all_certain_entities = pickle.load(file)[entity]

            pass
        except KeyError:
            return {}
    return all_certain_entities
