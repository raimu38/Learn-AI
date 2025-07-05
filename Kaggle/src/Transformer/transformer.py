import torch
import torch.nn as nn
import math

# 1. Scaled Dot-Product Attention
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super(ScaledDotProductAttention, self).__init__()
    
    def forward(self, Q, K, V, mask=None):
        d_k = Q.size(-1)
        # Q と K の転置を掛け合わせてスケール
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
        
        # マスクがある場合は、ゼロ部分を -inf に置換
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        # ソフトマックスで注意重みを計算
        attention_weights = torch.softmax(scores, dim=-1)
        
        # 注意重みと V の積を返す
        output = torch.matmul(attention_weights, V)
        return output, attention_weights

# 2. Multi-Head Attention
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super(MultiHeadAttention, self).__init__()
        # d_model はモデルの次元数、n_heads はヘッドの数
        assert d_model % n_heads == 0, "d_model は n_heads で割り切れる必要がある"
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        
        # Q, K, V 用の線形層
        self.W_Q = nn.Linear(d_model, d_model)
        self.W_K = nn.Linear(d_model, d_model)
        self.W_V = nn.Linear(d_model, d_model)
        
        # 各ヘッドの出力を連結した後の線形変換
        self.fc = nn.Linear(d_model, d_model)
        self.attention = ScaledDotProductAttention()
        
    def forward(self, q, k, v, mask=None):
        batch_size = q.size(0)
        
        # 線形変換後、ヘッド数に分割する。transpose でヘッドの次元を前に出す
        Q = self.W_Q(q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2)
        K = self.W_K(k).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2)
        V = self.W_V(v).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2)
        
        # 各ヘッドごとに Scaled Dot-Product Attention を適用する
        attn_output, attn_weights = self.attention(Q, K, V, mask)
        
        # 各ヘッドの出力を連結する
        attn_output = attn_output.transpose(1,2).contiguous().view(batch_size, -1, self.d_model)
        
        # 最終的な線形変換を適用する
        output = self.fc(attn_output)
        return output, attn_weights

# 3. Position-wise Feed-Forward Network
class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super(FeedForward, self).__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# 4. Transformer Encoder Layer (残差接続＋層正規化付き)
class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, n_heads)
        self.feed_forward = FeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x, mask=None):
        # マルチヘッド・アテンション → 残差接続 + 層正規化
        attn_output, attn_weights = self.self_attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_output))
        
        # FFN → 残差接続 + 層正規化
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))
        return x, attn_weights

# サンプル利用：ランダムな入力に対してエンコーダ層を実行してみる
if __name__ == "__main__":
    # ハイパーパラメータの設定
    d_model = 512      # 埋め込みベクトルの次元数
    n_heads = 8        # アテンションヘッドの数
    d_ff = 2048        # FFN 内部の次元数
    seq_length = 10    # シーケンスの長さ
    batch_size = 2     # バッチサイズ
    
    # [batch_size, seq_length, d_model] のランダムテンソルを作成
    sample_input = torch.rand(batch_size, seq_length, d_model)
    print(sample_input)
    
    # マスクはここでは使用せん（None にする）
    mask = None
    
    # Transformer エンコーダ層をインスタンス化
    encoder_layer = TransformerEncoderLayer(d_model, n_heads, d_ff, dropout=0.1)
    
    # 入力をエンコーダ層に通す
    encoder_output, attention_weights = encoder_layer(sample_input, mask)
    
    print("Encoder output shape:", encoder_output.shape)
    print("Attention weights shape:", attention_weights.shape)
