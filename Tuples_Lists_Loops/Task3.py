playlist = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
play_number = int(input('Enter how many how many petals you want to extract:'))

if play_number in range(1, 7):
    ans = playlist[play_number - 1]
    print(f'a prediction for the day: {ans}')
elif play_number >= 7:
    general_amount = len(playlist)
    ind = (play_number - 1) % general_amount
    ans_1 = playlist[ind]
    print(f'a prediction for the day: {ans_1}')
elif play_number <= 0:
    print(f'The number {play_number} is not valid.')
