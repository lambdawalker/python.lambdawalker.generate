def test_smoke():
    from lambdawalker.generate.field.firs_name import generate_first_name
    from lambdawalker.generate.field.last_name import generate_last_name
    from lambdawalker.generate.field.address import generate_road_name, generate_city_name
    from lambdawalker.generate.field.institutions import generate_voting_institution_name
    
    fn = generate_first_name()
    ln = generate_last_name()
    road = generate_road_name()
    city = generate_city_name()
    inst = generate_voting_institution_name()
    
    assert fn["data"]
    assert ln["data"]
    assert road["data"]
    assert city["data"]
    assert inst["data"]
    print("generate OK")
