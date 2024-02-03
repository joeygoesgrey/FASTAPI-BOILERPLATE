from fastapi import APIRouter, Depends, status, HTTPException 
from app.core.config import config
from app.schemas.auth_schemas import RefreshToken, RefreshTokenSchema
from app.core.utils import JwtService, Verify_password, Hash_password, TokenHelper
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.db import get_async_session
from app.models import User
from app.schemas.api_main_schemas import EmailValidate

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


async def token(form_data: OAuth2PasswordRequestForm=Depends()):
    email = form_data.username  # Treated 'username' as 'email'
    password = form_data.password
    if email and password:
        try:
            user_email = EmailValidate(email=email)  
        except Exception as e:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
        # Query the User model to check if the email exists
        user = await User.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
        # Check if the provided password matches the stored password
        if not Verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
        # Generate access and refresh tokens
        return {"access_token": TokenHelper.encode(
                payload={"user_id": user.id},
                expire_period=config.ACCESS_TOKEN_EXPIRE_MINUTES
            ), "refresh_token": TokenHelper.encode(
                payload={"sub": "refresh", "user_id": user.id},
                expire_period=config.REFRESH_TOKEN_EXPIRE_DAYS,
                is_access_token=False
            ), "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

@auth_router.post(
    "/refresh-token",
    response_model=RefreshToken,
)
async def refresh_token(request: RefreshTokenSchema):
    token = await JwtService().create_refresh_token(
     refresh_token=request.refresh_token
    )
    return {"access_token": token.access_token, "refresh_token": token.refresh_token}

