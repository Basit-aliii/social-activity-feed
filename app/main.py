from fastapi import FastAPI
from app.db import init_db
from app.routers import auth, posts, likes, follow, block, activity

app = FastAPI(title="Social Activity Feed API")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(follow.router, prefix="/follow", tags=["Follow"])
app.include_router(block.router, prefix="/block", tags=["Block"])
app.include_router(activity.router, prefix="/activity", tags=["Activity"])

@app.on_event("startup")
async def on_startup():
    await init_db()
