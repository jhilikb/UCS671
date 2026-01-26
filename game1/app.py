import streamlit as st
import random
import time

# -------------------------------
# Initialize session state
# -------------------------------
if "position" not in st.session_state:
    st.session_state.position = 0
    st.session_state.goal = 11
    st.session_state.q_index = 0
    st.session_state.coins = 0  # Collected coins

if "game1_completed" not in st.session_state:
    st.session_state.game1_completed = False

if "game2_completed" not in st.session_state:
    st.session_state.game2_completed = False

if "game3_completed" not in st.session_state:
    st.session_state.game3_completed = False



coin_placeholder = st.empty()
def show_coin_animation():
    frames = ["💰", "💰✨", "💰✨🪙", "💰✨"]
    for frame in frames:
        coin_placeholder.markdown(f"<div style='font-size:40px; text-align:right;'>{frame} Coins: {st.session_state.coins}</div>", unsafe_allow_html=True)
        time.sleep(0.5)
# -------------------------------
# Sample Questions
# -------------------------------
questions = [
        {
            "q": "What is the fixed ip of the jetson device?",
            "options": ["192.168.55.100", "192.168.55.1", "192.168.0.0"],
            "answer": "192.168.55.1"
        },
        {
            "q": "How do i connect to my jetson device from my linux terminal after plugging my jetson device to my usb port",
            "options": ["ssh 192.168.55.1", "ssh 192.168.55.100", "ssh nvidia@192.168.55.1"],
            "answer": "ssh nvidia@192.168.55.1"
        },
        {
            "q": "192.168.55.100 is the fixed ip of?",
            "options": ["jetson device", "laptop(host) when connected to jetson", "router"],
            "answer": "laptop(host) when connected to jetson"
        },
        {
            "q": "My linux username is csed, i issued a command ssh 192.168.55.1 after plugging in my jetson. What happens?",
            "options": ["the command tries to log me into a csed account on the jetson", "the command tries to log me into the root account on the jetson", "the command doesnt try to log me in"],
            "answer": "the command tries to log me into a csed account on the jetson"
        },
        {
            "q": "Why do I get keygen errors while trying to connect my jetson?",
            "options": ["my kit is faulty", "i previously connected another jetson device(different physical address) with same ip", "i used wrong ip address"],
            "answer": "i previously connected another jetson device(different physical address) with same ip"
        },
        {
            "q": "How do I remove keygen errors?",
            "options": ["use correct ip", "delete saved keys", "run again"],
            "answer": "delete saved keys"
        },
        {
            "q": "One difference between the jetson 2GB and 4GB",
            "options": ["data port and charging port are different for 4GB", "the data and charging port are same for both", "there is a separate charging port in 4gb, but the data port can be used for charging too"],
            "answer": "there is a separate charging port in 4gb, but the data port can be used for charging too"
        },
        {
            "q": "Which is a better option, OS on the sdcard or OS on the emmc",
            "options": ["sdcard if more memory is required", "emmc for small defined tasks", "sdcard is more flexible,emmc is for small targeted tasks"],
            "answer": "sdcard is more flexible,emmc is for small targeted tasks"
        },
        {
            "q": "Which linux is installed on jetson?",
            "options": ["Ubuntu", "Linux4Tegra (L4T)", "Fedora"],
            "answer": "Linux4Tegra (L4T)"
        },
        {
            "q": "How do I transfer a folder called data1 from jetson to my laptop connected to jetson?",
            "options": ["On the jetson terminal use scp nvidia@192.168.55.1:/home/nvidia/data1 ./ ", "On the laptop terminal use scp nvidia@192.168.55.1:/home/nvidia/data1 ./", "I cannot do it"],
            "answer": "On the laptop terminal use scp nvidia@192.168.55.1:/home/nvidia/data1 ./"
        },
        {
            "q": "How do I transfer a folder called fol1 from my laptop to my jetson?",
            "options": ["On the jetson terminal use scp nvidia@192.168.55.1:/home/nvidia/fol1 ./ ", "On the laptop terminal use scp ./fol1 nvidia@192.168.55.1:/home/nvidia/", "I cannot do it"],
            "answer": "On the laptop terminal use scp ./fol1 nvidia@192.168.55.1:/home/nvidia/"
        }
    ]


# -------------------------------
# Page styling
# -------------------------------
st.set_page_config(layout="wide")
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #87CEEB, #FFF);
}
# .stButton > button {
#     font-size: 60px;
#     padding: 15px;
#     width: 100%;
# }
[data-testid="column"] {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
</style>
""", unsafe_allow_html=True)

# st.markdown("""
# <style>
# /* Target Streamlit tab buttons */
# button[role="tab"] {
#     font-size: 30px ;
#     font-weight: bold ;
#     padding: 12px 20px ;
# }
# </style>
# """, unsafe_allow_html=True)
# -------------------------------
# Tabs
# -------------------------------
tab1, tab2 ,tab3,tab4 = st.tabs(["ℹ️ Instructions","🎮 GameLogin","🎮 GameDockerrun","🎮 GameDockerbuild"])

st.markdown("""
<style>
.stButton > button {
    font-size: 50px;
    background-color: green; 
    padding: 35px;
    width: 100%;
    color: white;
    font-weight: 600 ;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TAB 1: Game
# -------------------------------
with tab2:
    
    left, right = st.columns([1, 4], gap="large")  # 20/80 layout

    # Left: Character Image
    with left:
        st.image("Jetson.jpeg", width=300)

    # Right: Path + Quiz
    with right:
        # Draw path
        path = ""
        for i in range(st.session_state.goal + 1):
            if i == st.session_state.position:
                path += "🧍 "
            elif i == st.session_state.goal:
                path += "🍦 "
            else:
                path += "⬜ "
        st.markdown(
            f"<div style='font-size:60px; white-space:nowrap'>{path}</div>",
            unsafe_allow_html=True
        )

        # Win condition
        if st.session_state.position >= st.session_state.goal:
            st.session_state.game1_completed = True
            st.balloons()
            st.success("🎉 You reached the ice cream! You won!")
            st.session_state.position =0
            # st.stop()

        # Show current question
        q = questions[st.session_state.q_index % len(questions)]
        # st.subheader(q["q"])
        st.markdown(
    f"<div style='font-size:50px; font-weight:600;'>{q['q']}</div>",
    unsafe_allow_html=True
)

        for option in q["options"]:
            if st.button(option):
                if option == q["answer"]:
                    st.success("✅ Correct! Move forward 🚀")
                    st.session_state.position += 1
                    n=random.randint(0, 3)
                    st.session_state.coins += n
                    if n > 0:
                        show_coin_animation()
                else:
                    st.error("❌ Wrong! Move backward 😢")
                    st.session_state.position = max(0, st.session_state.position - 1)

                st.session_state.q_index += 1
                st.rerun()


    # Bottom pane: coins
    bottom_left, bottom_right = st.columns([3, 1])
    with bottom_right:
        st.markdown(
            f"<div style='font-size:60px; text-align:right;'>💰 Coins: {st.session_state.coins}</div>",
            unsafe_allow_html=True
        )

# -------------------------------
# TAB 2: Instructions
# -------------------------------
with tab1:
    st.header("How to Play")
    st.markdown("""
    <div style='font-size:50px; line-height:1.6;'>
    - Answer the questions on the right to move your character along the path.<br>
    - We will cover basic login details here <br> 
    - Correct answers move you forward and collect coins.<br>
    - Wrong answers move you backward.<br>
    - Reach the ice cream (🍦) at the end to win!<br>
    - Your collected coins are shown in the bottom-right corner.<br>
    - You unlock docker run and build levels on completing login level.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.8);
    color: #ff6600;
    font-size: 40px;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
">
    <div style="
        display: inline-block;
        padding-left: 100%;
        animation: roll 15s linear infinite;
    ">
        Try it yourself....NO cheating.....
    </div>
</div>

<style>
@keyframes roll {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-100%); }
}
</style>
""", unsafe_allow_html=True)
puzzles = [
    {
        "question": "Arrange the command to pull a pytorch docker image from a repository",
        "items": [
            "sudo",
            "Check the jetpack version 4.6 and match it with the software tag r32.6.1",
            "docker pull",
            "r32.6.1-pth2.0-py3",
            "nvcr.io/nvidia/l4t-pytorch:",
            ],
        "correct": [
            "Check the jetpack version 4.6 and match it with the software tag r32.6.1",
            "sudo",
            "docker pull",
            "nvcr.io/nvidia/l4t-pytorch:",
            "r32.6.1-pth2.0-py3",
        ],
        "reward": 3
    },
    {
        "question": "Arrange the command to run a docker image",
        "items": [
            "run",
            "sudo",
            "docker",
            "-it",
            "--network host",
            "nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth2.0-py3",
            "--runtime nvidia",
            "--device /dev/video0",
            "--volume /home/nvidia/Desktop/fol:/home/fol",
            "--rm",
        ],
        "correct": [
            "sudo",
            "docker",
            "run",
            "-it",
            "--rm",
            "--network host",
            "--runtime nvidia",
            "--device /dev/video0",
            "--volume /home/nvidia/Desktop/fol:/home/fol",
            "nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth2.0-py3",
                    

        ],
        "reward": 2
    },
    {
        "question": "View list of docker images in your device",
        "items": [
            "sudo",
            "images",
            "docker",
            ],
        "correct": [
            "sudo",
            "docker",
            "images",
        ],
        "reward": 1
    },
    {
        "question": "View list of containers in your device",
        "items": [
            "sudo",
            "-a",
            "ps",
            "docker",
            ],
        "correct": [
            "sudo",
            "docker",
            "ps",
            "-a"
        ],
        "reward": 1
    },
    {
        "question": "Create a new docker image via an existing container? 234578 is container_id, myimage:v1 is repo:tag name of new image",
        "items": [
            "sudo",
            "commit",
            "myimage:v1",
            "234578",
            "docker"
            ],
        "correct": [
            "sudo",
            "docker",
            "commit",
            "234578",
            "myimage:v1",
        ],
        "reward": 1
    },
]

if "puzzle_index" not in st.session_state:
    st.session_state.puzzle_index = 0


if "puzzle_order" not in st.session_state:
    st.session_state.puzzle_order = puzzles[0]["items"].copy()

def show_puzzle(puzzle):
    st.markdown(f"## 🧩 {puzzle['question']}")

    for i, item in enumerate(st.session_state.puzzle_order):
        col1, col2, col3 = st.columns([6,1,1])
        with col1:
            st.markdown(f"### {item}")
        with col2:
            if st.button("⬆️", key=f"up{i}") and i > 0:
                st.session_state.puzzle_order[i], st.session_state.puzzle_order[i-1] = \
                    st.session_state.puzzle_order[i-1], st.session_state.puzzle_order[i]
                st.rerun()
        with col3:
            if st.button("⬇️", key=f"down{i}") and i < len(st.session_state.puzzle_order)-1:
                st.session_state.puzzle_order[i], st.session_state.puzzle_order[i+1] = \
                    st.session_state.puzzle_order[i+1], st.session_state.puzzle_order[i]
                st.rerun()


with tab3:
    if not st.session_state.game1_completed:
        st.warning("🔒 Complete the game in Tab 1 to unlock this level.")
        st.image("Lock.jpeg", width=200)

    else:
        st.markdown(
            f"<div style='font-size:60px; text-align:right;'>💰 Coins: {st.session_state.coins}</div>",
            unsafe_allow_html=True
        )
        # Ensure puzzle_order is valid when tab unlocks
        if len(st.session_state.puzzle_order) == 0:
            st.session_state.puzzle_order = puzzles[
                st.session_state.puzzle_index 
            ]["items"].copy()

        current = puzzles[st.session_state.puzzle_index% len(puzzles)]

        show_puzzle(current)

        if st.button("✅ Check Answer",disabled=st.session_state.game2_completed):
            if st.session_state.puzzle_order == current["correct"]:
                st.success("🎉 Correct order!")
                st.session_state.coins += current["reward"]


                st.session_state.puzzle_index+=1

                if st.session_state.puzzle_index < len(puzzles):
                    st.session_state.puzzle_order = puzzles[
                        st.session_state.puzzle_index
                    ]["items"].copy()
                    st.rerun()
                else:
                    st.session_state.game2_completed=True
                    st.balloons()
                    st.success("🏆 All puzzles completed!")
                    time.sleep(0.9)

                    st.rerun()
            else:
                st.error("❌ Not correct yet, try again")


match_questions = [
    {
        "question": "Match the docker run concepts",
        "pairs": {
            "sudo": "to run docker with permission",
            "-it": "work with interactive mode on docker launch",
            "--rm": "delete container on exit",
            "--device /dev/video0": "add devices like camera",
            "--network host": "use jetsons(host for docker) wifi/lan inside docker",
            "--volume /home/nvidia/Desktop/fol:/home/fol": "mount jetsons folder fol inside docker /home",
        },
        "reward": 3
    },
    {
        "question": "Justify the following",
        "pairs": {
            "if i want to retain changes inside the container": "dont run using --rm",
            "if i dont have any cameras on jetson": "dont use --device /dev/video0 while running docker",
            "i want to add more softwares inside docker image": "run docker without rm, install via pip/apt, commit container after exit",
            "i want to add more data inside docker image": "run docker without rm, create data,add via git/wget, commit container after exit",
            "i have run docker with rm, mounted a jetson folder with --volume, can i retain data created inside docker?": "data created inside the mounted volume is retained without commit so no problem with rm",
        },
        "reward": 2
    },
    {
        "question": "Complete the following",
        "pairs": {
            "i want to build a docker from scratch": "add all commands inside a file called Dockerfile and build it",
            "what command do i use for building a docker": "sudo docker build -t mynewdoc:v2 .",
            "docker build and commit are same things": "both can create a new docker image, build may or may not use an existing image, commit uses a running container",
    },
        "reward": 2
    },
    {
        "question": "When i build a docker using a Dockerfile, the following Dockerfile keywords (written inside Dockerfile) can help me:",
        "pairs": {
            "i want to use an existing docker": "FROM repo:tag",
            "i want to git clone inside /home/pose folder in docker ": "WORKDIR /home/pose; RUN git clone xxxxx",
            "i want to run a t.sh file": "source t.sh",
            "i want to copy a folder pac1 from jetson inside the docker": "COPY pac1 /home/pose/",
            "i want to install a package matplotlib inside the docker using Dockerfile": "RUN pip install matplotlib",
        },
        "reward": 2
    }
]

if "match_index" not in st.session_state:
    st.session_state.match_index = 0

if "match_answers" not in st.session_state:
    st.session_state.match_answers = {}


def show_match_question(mq):
    st.markdown(f"## 🔗 {mq['question']}")

    options = list(mq["pairs"].values())
    random.shuffle(options)

    for left, correct_right in mq["pairs"].items():
        col1, col2 = st.columns([3, 3])

        with col1:
            st.markdown(f"### {left}")

        with col2:
            st.session_state.match_answers[left] = st.selectbox(
                "Match with",
                options,
                key=f"match_{left}",
                label_visibility="collapsed"
            )

def check_match_answer(mq):
    for left, right in mq["pairs"].items():
        if st.session_state.match_answers.get(left) != right:
            return False
    return True


with tab4:
    if not st.session_state.game2_completed:
        st.warning("🔒 Complete previous levels to unlock this tab")
    else:
        st.markdown(
            f"<div style='font-size:60px; text-align:right;'>💰 Coins: {st.session_state.coins}</div>",
            unsafe_allow_html=True
        )
        current = match_questions[st.session_state.match_index % len(match_questions)]

        show_match_question(current)

        if st.button("✅ Check Matches", disabled=st.session_state.game3_completed):
            if check_match_answer(current):
                st.success("🎉 All matches correct!")
                st.session_state.coins += current["reward"]

                st.session_state.match_index += 1
                st.session_state.match_answers = {}

                if st.session_state.match_index < len(match_questions):
                    st.rerun()
                else:
                    st.balloons()
                    st.success("🏆 All matching questions completed!")
                    st.session_state.game3_completed=True
                    time.sleep(0.9)
                    st.rerun()
            else:
                st.error("❌ Some matches are incorrect. Try again.")
