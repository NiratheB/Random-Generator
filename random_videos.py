import random


class Videos:
    # List of all videos
    all_video_list = []
    categories = ["Funny", "Sad", "Happy", "Anger", "Surprise"]
    emotions = ["Pos", "Neg", "Neu"]
    number_of_videos_per_survey = 4

    def __init__(self):
        self.videos = []


    @staticmethod
    def fill_all_videos():
        Videos.all_video_list = []
        for i in range(1, 101):
            category = random.choice(Videos.categories)
            emotion = random.choice(Videos.emotions)
            code = "Video"+str(i)
            Videos.all_video_list.append({"code": code, "category": category, "emotion": emotion})

    def get_watched_videos(self):
        pass

    def get_unwatched_videos(self, watched_videos):
        unwatched_video_list = Videos.all_video_list
        # if not all videos have been watched
        if len(watched_videos) < len(unwatched_video_list):
            # remove the watched videos
            for video in watched_videos:
                if video in unwatched_video_list:
                    unwatched_video_list.remove(video)
        return unwatched_video_list

    def check_duplicacy(self, selected_video):
        if len(self.videos) < 1:
            return False

        for video in self.videos:
            if selected_video["category"] == video["category"]:
                return True

        last_index = len(self.videos) - 1
        if selected_video["emotion"] == self.videos[last_index]["emotion"]:
            return True

        return False

    # get random videos eliminating those watched before
    def get_random_videos(self,watched_videos):
        self.videos = []
        video_list = self.get_unwatched_videos(watched_videos)
        random_indices = list(range(0,len(video_list)))
        random.shuffle(random_indices)
        selected_count = 0
        index = 0
        check_count = 0
        while selected_count < Videos.number_of_videos_per_survey:
            video_index = random_indices[index]
            selected_video = video_list[video_index]

            if not self.check_duplicacy(selected_video):
                self.videos.append(selected_video)
                selected_count += 1
                check_count = 0
            else:
                check_count += 1

            index += 1

            if index >= len(random_indices) or check_count >= len(video_list):
                video_list = Videos.all_video_list
                random_indices = list(range(0,len(video_list)))
                random.shuffle(random_indices)
                index = 0
                check_count = 0

        for video in self.videos:
            print(video["code"])

        return self.videos


Videos.fill_all_videos()
command = input("Press y to generate videos for you: ")
videos = Videos()
watched_videos = []
while command == 'y':
    video_list = videos.get_random_videos(watched_videos)
    print("You are watching :")
    print(video_list)
    watched_videos.extend(video_list)
    command = input("Press y to generate more videos for you: ")

