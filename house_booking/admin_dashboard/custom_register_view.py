from rest_framework import status
from rest_framework.response import Response
from allauth.account.views import RegisterView
from django.core.mail import send_mail
import logging

# Configure the logger
logger = logging.getLogger(__name__)

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Assuming the user has been successfully created
        if response.status_code == status.HTTP_201_CREATED:
            user = self.user
            user_email = user.email
            user_username = user.username

            # Send a custom welcome email
            send_mail(
                'Welcome to Our Service',
                'Hi {},\n\nThank you for registering with our service!'.format(user_username),
                'from@example.com',
                [user_email],
                fail_silently=False,
            )

            # Log registration details
            logger.info('New user registered: Username: {}, Email: {}'.format(user_username, user_email))
            
            # Add custom message to the response
            response.data['custom_message'] = 'Custom registration successful!'
        
        return Response(response.data, status=status.HTTP_201_CREATED)
