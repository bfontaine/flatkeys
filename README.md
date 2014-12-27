## Usage

    from flatdicts import flatdict

    d = {"foo": {"bar": 42}}
    print flatdict(d)
    # => {"foo.bar": 42}
