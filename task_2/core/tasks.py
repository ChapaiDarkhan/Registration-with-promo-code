from core.models import InvitationCode
from core.models import User


def add_invitation_bonus(promo_code):
    while promo_code:
        invitation_code = InvitationCode.objects.filter(invitation_code=promo_code).first()
        if invitation_code:
            user = User.objects.filter(id=invitation_code.user.id).first()
            user.bonus += 1
            user.save()
            promo_code = user.promo_code
