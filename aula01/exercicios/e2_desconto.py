# Crie 2 variáveis:
#   - cliente_vip
#   - cupom_desconto
#
# Ao final, imprima se o cliente tem direito ao desconto.
# O cliente tem direito ao desconto se for cliente VIP, mas
# também pode ter se possuir um cupom de desconto.

cliente_vip = True
cupom_desconto = False

if cliente_vip or cupom_desconto:
    print("O cliente tem direito ao desconto.")
else:
    print("O cliente não tem direito ao desconto.")