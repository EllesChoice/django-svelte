def ReadAllProfilesEntryReturnJSON():

    def convert_datetimes(d):
        for k, v in d.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()
        return d

    profiles = Profile.select()
    profiles_dicts = [convert_datetimes(model_to_dict(p)) for p in profiles]
    profiles_json = json.dumps(profiles_dicts)
    print(profiles_json)


    