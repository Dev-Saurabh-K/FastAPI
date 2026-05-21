from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {    
    1: {"title": "New Post", "content": "Cool text post"},
    2: {"title": "Python Basics", "content": "Learn variables and data types"},
    3: {"title": "FastAPI Guide", "content": "Building APIs with FastAPI"},
    4: {"title": "Web Development", "content": "Frontend meets backend"},
    5: {"title": "Database Tips", "content": "Understanding SQL and NoSQL"},
    6: {"title": "Machine Learning", "content": "Introduction to ML concepts"},
    7: {"title": "React Tutorial", "content": "Creating interactive UIs"},
    8: {"title": "Docker Essentials", "content": "Containerizing applications"},
    9: {"title": "Git Workflow", "content": "Version control best practices"},
    10: {"title": "Cloud Computing", "content": "Deploying apps to the cloud"},
    11: {"title": "REST APIs", "content": "Designing scalable APIs"},
    12: {"title": "Authentication", "content": "JWT and user login systems"},
    13: {"title": "Cyber Security", "content": "Protecting web applications"},
    14: {"title": "Data Structures", "content": "Arrays, stacks, and queues"},
    15: {"title": "Algorithms", "content": "Sorting and searching techniques"}
    }

@app.get("/posts")
def get_all_posts(limit: int = None):
    # print(list(text_posts.values())[:9])
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content":post.content}
    # print(text_posts.keys())
    text_posts[max(text_posts.keys())+1] =new_post
    return new_post

