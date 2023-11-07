# Oh wuhoh, you have a variable ammount of numbers that you would like to average. try it


# keep looping for inputs until the 
def avrg(*args):
    #####################
    count = 0
    combiner = 0
    #####################
    for number in args:
        combiner += number
        count += 1
    ####################
    if number == 0:
        return 0
    #####################
    return combiner / count
