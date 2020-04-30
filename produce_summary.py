def generate_produce_summary(one_file):

    for line in one_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    one_file.close()



def run_multiple_reports(list_of_files):
    for i, one_file in enumerate(list_of_files):
        print("Day", i+1)
        generate_produce_summary(one_file)


the_files = [open("um-deliveries-20140519.txt"),open("um-deliveries-20140520.txt"),open("um-deliveries-20140521.txt")]

run_multiple_reports(the_files)

