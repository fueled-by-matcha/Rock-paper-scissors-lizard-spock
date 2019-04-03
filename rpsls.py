def rpsls(p1,p2):
        """
Simple game of rock, paper, scissors

:type p1: string, == 'R' or 'S' or 'P'
:type p2: string, == 'R' or 'S' or 'P'
:rtype: int

    """
    if p1 == p2:
        return 0
    if p1 == 'R' and p2 == 'S':
        return -1
    elif p1 == 'P' and p2 == 'R':
        return -1
    elif p1 == 'S' and p2 == 'P':
        return -1
    else:
        return 1
