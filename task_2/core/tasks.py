from core.models import InvitationCode
from core.models import Profile


def add_invitation_bonus(promo_code):
    user_promo_code = promo_code
    while user_promo_code:
        invitation_code = InvitationCode.objects.filter(invitation_code=user_promo_code).first()
        if invitation_code:
            profile = Profile.objects.filter(id=invitation_code.profile.id).first()
            profile.bonus += 1
            profile.save()
            user_promo_code = profile.promo_code
