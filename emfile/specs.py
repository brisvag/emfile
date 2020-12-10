# full spec is at https://github.com/dtegunov/tom/blob/master/IOfun/tom_emread.m
header_spec = {
    'machine':      'b',
    'version':      'b',
    'unused':       'b',
    'dtype':        'b',
    'xdim':         'i',
    'ydim':         'i',
    'zdim':         'i',
    'comment':      '80s',
    'U':            'i',
    'COE':          'i',
    'APE':          'i',
    'VE':           'i',
    'VN':           'i',
    'ET':           'i',
    'OBJ':          'i',
    'EM':           'i',
    'CCD':          'i',
    'L':            'i',
    'DF':           'i',
    'FA':           'i',
    'PHI':          'i',
    'DDF':          'i',
    'CTS':          'i',
    'C2':           'i',
    'EW':           'i',
    'EO':           'i',
    'KW':           'i',
    'KR':           'i',
    'unknown1':     'i',
    'SC':           'i',
    'unknown2':     'i',
    'markerpos_x':  'i',
    'markerpos_y':  'i',
    'resolution':   'i',
    'density':      'i',
    'contrast':     'i',
    'unknown3':     'i',
    'SPx':          'i',
    'SPy':          'i',
    'SPz':          'i',
    'H':            'i',
    'unknown4':     'i',
    'D1':           'i',
    'D2':           'i',
    'lambda':       'i',
    'delta_theta':  'i',
    'unknown5':     'i',
    'unknown6':     'i',
    'username':     '20s',
    'date':         '8s',
    'padding':      '228x',
}

dtype_spec = {
    1:  'b',
    2:  'h',
    4:  'i',
    5:  'f',
    8:  '2f',    # ??
    9:  'd',
    10: '2d',    # ??
}
